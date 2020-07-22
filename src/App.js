import React from 'react';
import './App.css';
import Table from './components/Table';
import MultipleSelect from './components/Drop1';    
import DateAndTimePicker from './components/DateTime';             

function App() {

  function refreshPage() {
    //function to refresh this page
    window.location.reload(false);
  }


  return (
    <div className="App">
      
      <div className="App-header" >
        <h1 style={{color:'#137997'}}>Dashboard: Error Logs</h1>
        <div className="SameLine">
        <MultipleSelect/>
        <DateAndTimePicker/>
        <DateAndTimePicker/>
        </div>
        <div className="SameLine">
        <button onClick={()=>{alert("Filters applied!")}}>APPLY FILTERS</button>
        <button onClick={refreshPage} >RELOAD!</button>
        </div>
       <div ><Table/></div>
        
      </div>
      
      
         
    </div>
  );
}

export default App;
