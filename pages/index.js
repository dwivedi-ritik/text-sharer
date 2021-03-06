import React from 'react'
import InputBar from '../component/input'
import Head from "next/head"

const home = () => {
  return (
    <React.Fragment>
      <Head>
        <title>Text Share App</title>
      </Head>
      <div className="page-bg">
        <div className="arranger">
          <div className="heading">
            <p>A TEXT SHARE WEB APPLICATION!</p>
          </div>
          <div className="heading-desc">
            <p>Text sharer is simple web app made using next js. It is uses minimal design and
              redis lab as a database to store text and numeric code!</p>
            <ul>
              <li>Paste your text </li>
              <li>or Paste the code to retrive text</li>
              <li>After that hit search. </li>
              <li>Result will be shown in Result box</li>
            </ul>
          </div>

          <InputBar />
        </div>
      </div>
    </React.Fragment >
  )
}

export default home