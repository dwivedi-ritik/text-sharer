import React from 'react'
import Timer from './Timer'

const ResultBox = (props) => {
    let showtimer;
    if (props.result.new_key) {
        showtimer = <Timer value={0} />
    } else {
        showtimer = null
    }
    return (
        <React.Fragment>
            {showtimer}
            <div className="res-bar">
                <div className="res-title">
                    <p>RESULT</p>
                </div>
                <div className="res-result">{props.result.response}</div>
            </div>
        </React.Fragment>
    )
}

export default ResultBox