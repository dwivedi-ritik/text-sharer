import React from 'react'

const ResultBox = (props) => {
    return (
        <div className="res-bar">
            <div className="res-title">
                <p>RESULT</p>
            </div>
            <div className="res-result">{props.result}</div>
        </div>
    )
}

export default ResultBox