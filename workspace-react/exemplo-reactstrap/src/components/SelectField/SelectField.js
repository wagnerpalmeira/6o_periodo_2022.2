import React from 'react';

const SelectField = (props) => {
    return (
        <select>
            {props.options.map(option => {
                return (
                    <option key={option}>{option}</option>
                )
            })}
        </select>
    )
}

export default SelectField;