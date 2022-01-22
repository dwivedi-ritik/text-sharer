import React from 'react'
import { useState } from 'react'

import ResultBox from './ResultBox'

const InputBar = () => {
    let timer = null
    let [jsonValue, setjsonValue] = useState({})
    let [inpValue, setValue] = useState('')

    let json_reply = {}

    const perform_db = async (e) => {
        e.preventDefault()
        if (inpValue.length < 1000) {

            const res = await fetch("/api/redis_api", {
                method: "post",
                body: JSON.stringify({ usrInp: inpValue })
            })

            json_reply = await res.json()
            setjsonValue(json_reply)
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