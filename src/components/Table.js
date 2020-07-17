import React, { Component } from 'react'
import axios from 'axios'

class Table extends Component {
   constructor(props) {
      super(props) //since we are extending class Table so we have to use super in order to override Component class constructor
      this.state = { //state is by default an object
         records: [
            {
                  "timestamp8601": "2020-07-14T12:53:40",
                  "cf_app_name": "support-home-ux",
                  "Exception_Name": "System.Exception",
                  "Error_Message": " home-critical-application-exception: Exception of type 'System.Exception' was thrown. error path: /support/home/nl-nl , corrId- customstr101= , customnb101=500 ",
                  "Exception_Details": " System.Exception: Exception of type 'System.Exception' was thrown. ->    at Dell.SupportOnline.Web.Middleware.RequestValidationModule.Invoke(HttpContext httpContext) ->    at Dell.SupportOnline.Common.Middleware.SecurityHeadersMiddleware.InvokeAsync(HttpContext httpContext) ->    at Microsoft.AspNetCore.ResponseCaching.ResponseCachingMiddleware.Invoke(HttpContext httpContext) ->    at Microsoft.AspNetCore.Cors.Infrastructure.CorsMiddleware.Invoke(HttpContext context) ->    at Dell.SupportOnline.Home.Web.Dependency.LwpCultureUrlRedirectMiddlewareExtended.Invoke(HttpContext httpContext, IConfiguration configuration, ILogger`1 logger) in /builds/services/esupport/home/src/Dell.SupportOnline.Home.Web/Dependency/LwpCultureUrlRedirectMiddlewareExtended.cs:line 119 ->    at Dell.Identity.WebModule.Core.Middlewares.DaisAuthenticationMiddleware.Invoke(HttpContext context) ->    at Microsoft.AspNetCore.StaticFiles.StaticFileMiddleware.Invoke(HttpContext context) ->    at Dell.SupportOnline.Home.Web.Startup.<>c.<<Configure>b__8_0>d.MoveNext() in /builds/services/esupport/home/src/Dell.SupportOnline.Home.Web/Startup.cs:line 79 -> --- End of stack trace from previous location where exception was thrown --- ->    at Microsoft.AspNetCore.Builder.Extensions.UsePathBaseMiddleware.Invoke(HttpContext context) ->    at Microsoft.AspNetCore.Diagnostics.ExceptionHandlerMiddleware.Invoke(HttpContext context) "
            },
            {
                  "timestamp8601": "2020-07-14T12:52:02",
                  "cf_app_name": "flatcontents-ux",
                  "Exception_Name": "System.Exception",
                  "Error_Message": " Service Response Error: MetaDocument service response does not contain dellCategoryList , -corId=> customstr101=ab421617-36db-4259-63d7-1a1b5aaba5ad , customstr102=Exception  ",
                  "Exception_Details": " System.Exception: dellCategoryList Missing in service response "
            },
            {
                "timestamp8601": "2020-07-14T12:52:03",
                "cf_app_name": "drivers-ux",
                "Exception_Name": "System.Exception",
                "Error_Message": " Service Response Error: MetaDocument service response does not contain dellCategoryList , -corId=> customstr101=ab421617-36db-4259-63d7-1a1b5aaba5ad , customstr102=Exception  ",
                "Exception_Details": " System.Exception: dellCategoryList Missing in service response "
          }
      ]
      }
   }

   componentDidMount(){
       axios.get('http://127.0.0.1:8089/filterData?app_i=support-home-ux&app_x=flatcontents-ux&st=2020-07-14T12:50:21.309Z&et=2020-07-14T12:56:34.975Z')
       .then(response=>{
           console.log(response)
           this.setState({records:response.data})
       })
       .catch(error=>{
           console.log(error)
       })

   }

   renderTableData() {
    return this.state.records.map((record, index) => {
       const { Exception_Details,timestamp8601,  Error_Message,cf_app_name, Exception_Name } = record //destructuring
       return (
          <tr key={timestamp8601}>
             <td>{Exception_Details}</td>
             <td>{timestamp8601}</td>
             <td>{Error_Message}</td>
             <td>{cf_app_name}</td>
             <td>{Exception_Name}</td>
          </tr>
       )
    })
 }

 renderTableHeader() {
   
    let header = Object.keys(this.state.records[0])
    return header.map((key, index) => {
       return <th key={index} >{key.toUpperCase()}</th>
    })
 }

 render() {
    return (
       <div>
          <table id='records' border='1px'   >
             <tbody>
             <tr border-collapse='collapse'>{this.renderTableHeader()}</tr>
                {this.renderTableData()}
             </tbody>
          </table>
       </div>
    )
 }
}



export default Table;