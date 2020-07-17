import React from 'react';
import './App.css';
import Table from './components/Table';
import MultipleSelect from './components/Drop1';    
//import SimpleTable from './components/Sample';                 

function App() {

  function refreshPage() {
    //function to refresh this page
    window.location.reload(false);
  }


  return (
    <div className="App">
      <body className="App-body">
      <div className="App-header" >
        <h1 style={{color:'#137997'}}>Dashboard: Error Logs</h1>
        <MultipleSelect/>
        <div className="SameLine">
        <button onClick={()=>{alert("Filters applied!")}}>APPLY FILTERS</button>
        <button onClick={refreshPage} >RELOAD!</button>
        </div>
        <Table/>
      </div>
      
      </body>
         
    </div>
  );
}

export default App;
