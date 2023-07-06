import React,{useState} from "react"

const Calculate1=()=>{

    const [op,setOp]=useState()
    const [num1,setNum1]=useState()
    const [num2,setNum2]=useState()
    const [res,setRes]=useState()

    const Calculate=()=>{
        if(op === '+'){
           let res = parseInt(num1)+parseInt(num2)
            setRes(res)
        }
        else if(op === '-'){
            let res = parseInt(num1)-parseInt(num2)
            setRes(res)
        }
        else if(op === '/'){
           let res = parseInt(num1)/parseInt(num2)
            setRes(res)
        }
        else if(op === '*'){
            let res = parseInt(num1)*(parseInt(num2))
            setRes(res)
        }
        else{
            let res = "Invalid Operator"
            setRes(res)
        }
        
    }

    return(

        <div>
            <h1>Simple Calculator</h1>
            <label>Operator: </label>
            <input value={op} onChange={(e)=>setOp(e.target.value)} placeholder="Enter Operator"></input><br/>
            <label>Number 1: </label>
            <input value={num1} onChange={(e)=>setNum1(e.target.value)} placeholder="Enter Number 1"></input><br/>
            <label>Number 2:</label>
            <input value={num2} onChange={(e)=>setNum2(e.target.value)} placeholder="Enter Number2"></input><br/>
            <button onClick={Calculate}>Calculate</button>
            <h1> {num1}{op}{num2} = {res}</h1>
            <h1>Calculated result {res}</h1>

        </div>
    )

}

export default Calculate1