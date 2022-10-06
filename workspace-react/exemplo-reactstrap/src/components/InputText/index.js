import './InputText.css';
import React from 'react';

const InputText = (props) => {

    const onInput = (e) => {
        props.onInput(e.target.value)
    }

    return (
        <div className="input-text">
            <label>{props.label}</label>
            <input value={props.valor} 
                    onChange={onInput} 
                    type="text" 
                    placeholder={props.placeholder}/>
        </div>
    );
}

export default InputText;