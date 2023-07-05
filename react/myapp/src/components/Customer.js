import React from 'react'
const Customer=()=>{
   let Custo = [
        {
            id:1,
            name: 'Balaji',
            location: 'Mumbai'
        },
        {
            id:2,
            name: 'Ravi',
            location: 'Maharashtra'
        },
        {
            id:3,
            name: 'Ram',
            location: 'Andhra'
        },
        {
            id:4,
            name: 'Bala',
            location: 'POnicherry'
        }
    ]
    return(
        <div>
        <table className='Table1'>
            
            <thead >
                <tr>
                    <th>id</th>
                    <th>Name</th>
                    <th>Location</th>
                </tr>
            </thead>
            <tbody>
                {
                    Custo.map((customer)=><tr><td>{customer.id}</td><td>{customer.name}</td><td>{customer.location}</td></tr>)
                }
            </tbody>
        </table>
        </div>
    )

}
export default Customer