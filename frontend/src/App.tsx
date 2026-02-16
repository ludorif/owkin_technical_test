import {useState} from 'react';
import SimpleTextForm from './Components/SimpleTextForm';
import axios, {type AxiosInstance, type AxiosResponse} from 'axios';
import './App.css';

interface Query
{
    question: string;
    //api_key: string to limit number of requests
}

interface Result
{
    answer: string;
}

const API_URL = import.meta.env.VITE_BACKEND_URL;

// Create axios instance
const api: AxiosInstance = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

const App = () =>
{
    const [question, setQuestion] =  useState<string>("");
    const [answer, setAnswer] = useState<string>("");
    const [query, setQuery] = useState<Query | null>(null);

    function Submit (e: React.FormEvent)
    {
        e.preventDefault();
        const query : Query = { question };

        api.post<Query, AxiosResponse<Result>>('/query/', query)
            .then(res =>
            {
                setQuery(query);
                setAnswer(res.data.answer);
                setQuestion("")
            })
            .catch(err => {
                console.log(err)
                setAnswer(err);
            });
    }


    return <div className="center-screen">
                {query && (
                    <div>
                        <p> <b>Question:</b> <br />{query.question} </p>
                        <p className="multiline"><b>Answer:</b> <br />{answer} </p>
                        <br/>
                    </div>
                    )}
                <div>
                    <form onSubmit={Submit}>
                        <SimpleTextForm name='Question'
                        onChange={(e)=> setQuestion(e.target.value)}  >
                        </SimpleTextForm>
                        <input style={{ width: "300px" }} type="submit" />
                    </form>
                </div>
    </div>

}

export default App;
