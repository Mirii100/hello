import './App.css';
import { useState } from 'react';
const Alex=(props) => {
  return(
  <>
   <h3>Name:{props.Name}</h3>
  </>);
}
const Main=(props)=>{
  return(<>
<h2>number:{props.Number};</h2>
<input name='props.name' placeholder='name' title='namee'/>
<h3>image:{props.image}</h3>
<img 
alt='hello'
src='C:\Users\njugu\OneDrive\Pictures\Camera Roll\WIN_20230314_18_08_40_Pro.jpg'/>
<div className='main'>
  <h2>Email:</h2>
  <input type='email'name='email' placeholder='joe@gmail.com'/>
</div>
</>
  )
}
const App= ()=> {
  const [counter,setCounter]=useState(0);
  //declaring name in arrow  function  
  
  return (
    <div className="App">
//demonstrates how props work
<h1><Alex Name="njuguna"/></h1>

<button onClick={()=>setCounter((prevCount)=>prevCount-1)}>-</button>
<h1>{counter}</h1>
<button onClick={()=>setCounter((prevCount)=>prevCount+1)}>+</button>
<div className='demo'>
  <div>
  <h1><Main Number="233"/></h1>
  <h3>
    <Main image= ''/></h3>
  </div>
</div>


   </div>

  );}

export default App;
