import React from 'react'
import InputBar from '../component/input'

const home = () => {
  return (
    <React.Fragment>
      <div className="page-bg">
        <div className="arranger">
          <div className="heading">
            <p>A TEXT SHARER WEB APPLICATION!</p>
          </div>
          <div className="heading-desc">
            <p>Text sharer is simple web app made using next js. It is uses minimal design and
              redis lab as a database to store text and numeric code.
              Welcome to the one of a kind club!</p>
          </div>

          <InputBar />
        </div>
      </div>
    </React.Fragment>
  )
}

export default home