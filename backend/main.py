import pandas as pd
from typing import List, Dict
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Query(BaseModel):
    question: str
    #api_key: str to limit number of requests 

class Result(BaseModel):
    answer: str

supported_cancers : set[str]
app = FastAPI()


def get_cancer_in_question(question: str) -> str | None:
    """ Return the cancer type in the question or None if not found """

    for cancer_type in supported_cancers:
        if cancer_type in question:
            return cancer_type
    return None

def get_cancer_types() -> set[str]:
    """Return a list of cancer types in our data."""
    return set(df['cancer_indication'])

def get_targets(cancer_name: str) -> List[str]:
    """Return a list of gene targets for a given cancer type."""
    return df[df['cancer_indication'] == cancer_name]['gene'].tolist()

def get_expressions(genes: List[str]) -> Dict[str, float]:
    """Return the median values for the given list of genes."""
    subset = df[df['gene'].isin(genes)]
    return dict(zip(subset['gene'], subset['median_value']))


@app.post("/query/")
def request(query : Query) -> Result:
    """Receive a query from a user, interpret the question and return a result from our data or an error message. """

    question = query.question.lower()

    if not question or "help" in question:
       return Result(answer = HELP_MESSAGE)
    
    cancer = get_cancer_in_question(question)

    if cancer is None:
        return Result(answer = CANCER_TYPE_ERROR)

    targets = get_targets(cancer)
    if "expression" in question or "median" in question:
        return Result(answer = str(get_expressions(targets)))
    elif "genes" in question or "target" in question:
        return Result(answer=str(targets))
    else:
        return Result(answer=QUESTION_ERROR)

# Load CSV
df = pd.read_csv("owkin_take_home_data.csv")
supported_cancers = get_cancer_types()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CANCER_TYPE_ERROR = "We did not understand the cancer type or we do not have enough data for this cancer type at this time."

QUESTION_ERROR = "We did not understand your question but we are working on improving our system, please share feedback."

HELP_MESSAGE = str("I can:\n"
                "- List main genes involved in a cancer type\n"
                "- Compute median gene expression values for a cancer type\n\n"
                "Supported cancers: " + str(supported_cancers))