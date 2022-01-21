import React from 'react'
import { useState } from 'react'

import ResultBox from './ResultBox'
const InputBar = () => {
    let [jsonValue, setjsonValue] = useState('')
    let [inpValue, setValue] = useState('')
    const perform_db = async (e) => {
        e.preventDefault()
        if (inpValue.length < 500) {

            const res = await fetch("/api/redis_api", {
                method: "post",
                body: JSON.stringify({ usrInp: inpValue })
            })

            let json_reply = await res.json()
            setjsonValue(json_reply.response)
        }
    }
    let placeholder = "TYPE IN YOUR CODE OR TEXT TO CONVERT"
    return (
        <React.Fragment>
            <div className="inp-btn-box">
                <form onSubmit={perform_db}>
                    <input className="inp-bar" type="text" placeholder={placeholder} value={inpValue} onChange={(e) => setValue(e.target.value)}></input>
                    <input className="submit-btn" type="submit" value="Search"></input>
                </form>
            </div >
            <ResultBox result={jsonValue} />
        </React.Fragment>
    )
}


export default InputBar