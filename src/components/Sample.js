import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import { FormHelperText } from '@material-ui/core';

const useStyles = makeStyles({
  table: {
    minWidth: 650,

  },
});

function createData(timestamp, cf_app_name, exception_name, error_message, exception_details) {
  return { timestamp, cf_app_name, exception_name, error_message, exception_details };
}

const rows = [
  createData('2020-07-14T12:53:40', 'support-home-ux', 'System.Exception', 'ome-critical-application-exception: Exception of type System.Exception was thrown. error path: /support/home/nl-nl , corrId- customstr101= , customnb101=500 ', 'System.Exception: Exception of type System.Exception was thrown. ->    at Dell.SupportOnline.Web.Middleware.RequestValidationModule.Invoke(HttpContext httpContext) ->    at Dell.SupportOnline.Common.Middleware.SecurityHeadersMiddleware.InvokeAsync(HttpContext httpContext) ->    at Microsoft.AspNetCore.ResponseCaching.ResponseCachingMiddleware.Invoke(HttpContext httpContext) ->    at Microsoft.AspNetCore.Cors.Infrastructure.CorsMiddleware.Invoke(HttpContext context) ->    at Dell.SupportOnline.Home.Web.Dependency.LwpCultureUrlRedirectMiddlewareExtended.Invoke(HttpContext httpContext, IConfiguration configuration, ILogger`1 logger) in /builds/services/esupport/home/src/Dell.SupportOnline.Home.Web/Dependency/LwpCultureUrlRedirectMiddlewareExtended.cs:line 119 ->    at Dell.Identity.WebModule.Core.Middlewares.DaisAuthenticationMiddleware.Invoke(HttpContext context) ->    at Microsoft.AspNetCore.StaticFiles.StaticFileMiddleware.Invoke(HttpContext context) ->    at Dell.SupportOnline.Home.Web.Startup.<>c.<<Configure>b__8_0>d.MoveNext() in /builds/services/esupport/home/src/Dell.SupportOnline.Home.Web/Startup.cs:line 79 -> --- End of stack trace from previous location where exception was thrown --- ->    at Microsoft.AspNetCore.Builder.Extensions.UsePathBaseMiddleware.Invoke(HttpContext context) ->    at Microsoft.AspNetCore.Diagnostics.ExceptionHandlerMiddleware.Invoke(HttpContext context)'),
  createData('2020-07-14T12:52:02', 'flatcontents-ux', 'System.Exception', 'Service Response Error: MetaDocument service response does not contain dellCategoryList', 'System.Exception: dellCategoryList Missing in service response '),
  
];

export default function SimpleTable() {
  const classes = useStyles();

  return (
    <TableContainer component={Paper}>
      <Table className={classes.table} aria-label="simple table" >
        <TableHead>
          <TableRow>
            <TableCell>TimeStamp</TableCell>
            <TableCell align="right">Application Name</TableCell>
            <TableCell align="right">Exception Name</TableCell>
            <TableCell align="right">Error Message</TableCell>
            <TableCell align="right">Exception Details</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.timestamp}>
              <TableCell component="th" scope="row">
                {row.timestamp}
              </TableCell>
              <TableCell align="right">{row.cf_app_name}</TableCell>
              <TableCell align="right">{row.exception_name}</TableCell>
              <TableCell align="right">{row.error_message}</TableCell>
              <TableCell align="right">{row.exception_details}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}