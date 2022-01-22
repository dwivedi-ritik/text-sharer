import React, { useEffect } from "react";
import { useState } from "react";

const DescribeTimer = (props) => {
    return (
        <div className="timer-comp">
            <p>Code will expire after 120 seconds </p>
            <p>Total time left {120 - props.time} seconds</p>
        </div>
    )
}

const DeadTimer = () => {
    return (
        <p className="expired-code">Code expired</p>
    )
}
const Timer = (props) => {
    const [time, setTime] = useState(props.value);

    const [deadTimer, setDeadTimer] = useState(false)

    useEffect(() => {
        let interval = null;

        interval = setInterval(() => {
            setTime((time) => time + 1);
            if (props.reset) {
                setTime(0)
            }
        }, 1000);

        if (time >= 120) {
            clearInterval(interval)

            setDeadTimer(true)
        }

        return () => clearInterval(interval);
    }, [time]);



    return (
        <React.Fragment>
            {deadTimer ? <DeadTimer /> : <DescribeTimer time={time} />}
        </React.Fragment>
    );
};

export default Timer