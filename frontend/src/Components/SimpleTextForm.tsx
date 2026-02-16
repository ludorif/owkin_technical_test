import React from "react";

interface SimpleTextFormProps
{
    name : string;
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const SimpleTextForm : React.FC<SimpleTextFormProps> = ({name, onChange}) =>
{

    return <>
        <div>
            <input style={{ width: "300px" }}
                type="text"
                placeholder={name}
                onChange={onChange}
            />
        </div>
    </>
}

export default SimpleTextForm;
