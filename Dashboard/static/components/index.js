console.log("starts")
let doneBtn = document.getElementById('apply-filter')
let chipList = []
let chipSet = new Set()
showChips()
//console.log(localStorage)
//console.log('hell')
let appsMap = new Map()
let appList = []
let appsSize = 0
let exceptionSize = 0
let timeMap = new Map()
let exceptionList = []
let exceptionMap = new Map()
let colors = ["rgba(110,57,42,0.3)", "rgba(36,2,114,0.6)", "rgba(178,250,226,0.9)", "rgba(171,253,56,0.0)", "rgba(177,147,20,0.2)", "rgba(125,156,38,0.7)", "rgba(158,132,222,0.1)", "rgba(28,118,29,0.0)", "rgba(149,201,179,0.4)", "rgba(247,207,79,0.1)", "rgba(161,49,201,0.7)", "rgba(58,129,36,0.2)", "rgba(79,17,145,0.8)", "rgba(188,10,148,0.8)", "rgba(189,249,89,0.5)", "rgba(58,61,29,0.9)", "rgba(105,153,47,0.4)", "rgba(208,160,83,0.1)", "rgba(168,53,120,0.2)", "rgba(28,117,191,0.5)", "rgba(90,221,14,0.7)", "rgba(179,65,166,1.0)", "rgba(143,94,103,0.7)", "rgba(240,91,227,0.0)", "rgba(242,104,76,0.7)", "rgba(37,171,140,0.1)", "rgba(147,128,23,0.5)", "rgba(140,151,63,0.1)", "rgba(69,229,77,0.8)", "rgba(250,88,156,0.8)", "rgba(140,177,200,1.0)", "rgba(170,64,91,0.2)", "rgba(154,229,167,0.1)", "rgba(143,244,233,0.2)", "rgba(194,212,154,0.3)", "rgba(9,6,65,0.4)", "rgba(242,246,60,0.9)", "rgba(91,40,90,0.4)", "rgba(193,4,184,0.7)", "rgba(158,248,193,0.4)", "rgba(18,130,243,0.1)", "rgba(32,242,131,0.3)", "rgba(156,244,14,0.6)", "rgba(51,117,240,0.3)", "rgba(116,141,17,0.3)", "rgba(217,226,68,0.8)", "rgba(253,250,4,0.6)", "rgba(125,81,6,0.1)", "rgba(173,82,255,0.8)", "rgba(128,190,192,0.3)", "rgba(191,169,149,0.5)", "rgba(203,84,210,0.8)", "rgba(195,176,219,0.5)", "rgba(81,170,221,1.0)", "rgba(222,254,176,0.7)", "rgba(21,122,89,0.4)", "rgba(193,24,66,0.7)", "rgba(134,150,160,0.9)", "rgba(88,40,193,0.4)", "rgba(187,116,134,1.0)", "rgba(218,165,216,0.8)", "rgba(246,149,95,0.1)", "rgba(75,136,92,0.0)", "rgba(131,56,93,0.2)", "rgba(177,121,137,0.0)", "rgba(252,91,96,0.2)", "rgba(79,71,224,0.8)", "rgba(207,21,224,0.2)", "rgba(242,24,94,0.8)", "rgba(76,170,16,0.5)", "rgba(94,248,130,0.8)", "rgba(132,40,160,0.5)", "rgba(171,203,50,0.0)", "rgba(141,234,19,0.5)", "rgba(82,240,147,0.0)", "rgba(216,87,252,0.0)", "rgba(32,147,181,0.8)", "rgba(152,154,64,0.8)", "rgba(74,15,252,0.4)", "rgba(105,116,213,0.6)", "rgba(86,77,50,0.5)", "rgba(216,239,184,0.0)", "rgba(210,190,127,0.6)", "rgba(156,20,70,0.9)", "rgba(64,138,152,0.1)", "rgba(209,127,252,0.1)", "rgba(194,38,118,0.3)", "rgba(236,15,166,0.9)", "rgba(98,59,59,0.1)", "rgba(8,165,42,0.1)", "rgba(175,200,47,0.2)", "rgba(114,19,6,0.7)", "rgba(215,219,253,0.6)", "rgba(109,18,189,0.8)", "rgba(250,180,20,1.0)", "rgba(203,114,133,1.0)", "rgba(229,53,134,0.3)", "rgba(149,189,210,0.9)", "rgba(20,243,227,0.2)", "rgba(220,55,220,0.9)"]


function random_rgba() {
    var o = Math.round, r = Math.random, s = 255;
    return 'rgba(' + o(r()*s) + ',' + o(r()*s) + ',' + o(r()*s) + ',' + r().toFixed(1) + ')';
}











document.getElementById('visual').addEventListener('click', function (e) {
    //console.log(e.type)
    //console.log(appsMap.size)
    if (appsSize == 0 && exceptionSize == 0) myChart.innerHTML = 'Please Choose an appropriata timestamp!'
    else {
        myChart.innerHTML = ''
        let labelz = []
        let labell = ''
        let datas = []
        let colorz = []
        let i = 0;
        if (appsSize >= exceptionSize) {

            labell = 'Applications'
            appList.forEach(function (element) {
                labelz.push(element)
                datas.push(appsMap.get(element))
                // colorz.push(colors[i])
                colorz.push(random_rgba())
                i = i + 1;
            });


        } else {
            labell = 'Exceptions'
            exceptionList.forEach(function (element) {
                labelz.push(element)
                datas.push(exceptionMap.get(element))
                // colorz.push(colors[i])
                colorz.push(random_rgba())
                i = i + 1;
            });

        }
        console.log(labelz)

        var ctx = document.getElementById('myChart').getContext('2d');
        var chart = new Chart(ctx, {
            // The type of chart we want to create
            type: 'doughnut',

            // The data for our dataset

            data: {
                labels: labelz,
                datasets: [{
                    label: labell,
                    backgroundColor: colorz,
                    data: datas
                }]
            },

            // Configuration options go here
            options: {}
        });
        console.log(labelz)







    }
});










doneBtn.addEventListener('click', function (e) {
    let category = document.getElementById('category-name')
    let operator = document.getElementById('operator-name')
    let items = document.getElementById('list')

    if (category.value == '' || operator.value == '' || items.value == '') console.log('please make a selection!')
    else {
        //console.log(localStorage)
        let notes = localStorage.getItem('chips');
        if (notes == null) {
            chipList = [];
        } else {
            chipList = JSON.parse(notes);
        }
        document.getElementById("close").click();
        chipList.push(category.value + ' ' + operator.value + ' ' + items.value)
        localStorage.setItem('chips', JSON.stringify(chipList));
        $('#category-name').val('');
        $('#operator-name').val('');
        let parentElement = document.getElementById('add-on')
        parentElement.innerHTML = `<input type="text" readonly placeholder="Select any" id="list" size="18" data-toggle="dropdown" aria-haspopup="true"
        aria-expanded="false" style="border-radius: 20px;border-color: black;transform:none;
        outline:none;background:transparent;padding-left: 5px;text-align: center;"><div class="dropdown-menu" style="border-radius: 2px;" id="list-item">`
        //console.log(chipList)
        //console.log('calling')
        showChips()

    }
});
$('#category a').on('click', function () {
    //console.log($(this).text());
    let app_list = ["IPSDashboard-UX", "support-ode-ux", "Documents-UX", "Advisories-UX", "guidedPath-ux-prod", "OrderStatusUX", "KbArticle-UX", "article-ux", "flatcontents-ux", "ProductSupport-UX", "security-portal-ux", "masthead-ux", "support-home-ux", "drivers-ux", "sonar-validator-ux"]
    $('#category-name').val($(this).text());
    let parentElement = document.getElementById('add-on')
    if ($(this).text() == "Application Name") {
        let htmlPart = `<input type="text" readonly placeholder="Select any" id="list" size="18" data-toggle="dropdown" aria-haspopup="true"
    aria-expanded="false" style="border-radius: 20px;border-color: black;transform:none;
    outline:none;background:transparent;padding-left: 5px;text-align: center;"><div class="dropdown-menu" style="border-radius: 2px;" id="list-item">`
        let subPart = ``
        app_list.forEach(function (element, index) {

            subPart += `<a class="dropdown-item">${element}</a>`;


        });
        htmlPart += subPart
        parentElement.innerHTML = htmlPart
    } else {
        parentElement.innerHTML = `<input type="text" readonly placeholder="Select any" id="list" size="18" data-toggle="dropdown" aria-haspopup="true"
        aria-expanded="false" style="border-radius: 20px;border-color: black;transform:none;
        outline:none;background:transparent;padding-left: 5px;text-align: center;">`
    }
    $('#list-item a').on('click', function () {
        //console.log($(this).text());
        $('#list').val($(this).text());
    });
});
$('#operator a').on('click', function () {
    //console.log($(this).text());
    $('#operator-name').val($(this).text());
});

let apply = document.getElementById('apply')
apply.addEventListener('click', function (e) {
    let startDate = document.getElementById('datepicker')
    let endDate = document.getElementById('datepicker1')
    if (startDate.value == '' || endDate.value == '') alert(`You cannot leave Date-time field as empty!`)
    else {
        let startTime = startDate.value.substr(6, 4) + '-' + startDate.value.substr(0, 2) + '-' + startDate.value.substr(3, 2) + 'T' + startDate.value.substr(11, 16) + ':00.000Z'
        let endTime = endDate.value.substr(6, 4) + '-' + endDate.value.substr(0, 2) + '-' + endDate.value.substr(3, 2) + 'T' + endDate.value.substr(11, 16) + ':00.000Z'
        if (startTime.localeCompare(endTime) <= 0) {
            //console.log(startTime.localeCompare(endTime))
            let urlLink = 'filterData?st=' + startTime + '&et=' + endTime
            let notes = localStorage.getItem('chips');
            if (notes == null) {
                chipList = [];
            } else {
                chipList = JSON.parse(notes);
            }
            chipSet = new Set(chipList)
            for (let item of chipSet) {
                if (item.indexOf('Application Name') != -1) {
                    if (item.indexOf('is not') != -1) {
                        let app_x = item.slice(item.indexOf('is not') + 7, item.length)
                        urlLink += '&app_x=' + app_x
                    }
                    else if (item.indexOf('is') != -1) {
                        let app_x = item.slice(item.indexOf('is') + 3, item.length)
                        urlLink += '&app_i=' + app_x
                    }
                }
                else if (item.indexOf('Exception Name') != -1) {
                    if (item.indexOf('is not') != -1) {
                        let app_x = item.slice(item.indexOf('is not') + 7, item.length)
                        urlLink += '&except_x=' + app_x
                    }
                    else if (item.indexOf('is') != -1) {
                        let app_x = item.slice(item.indexOf('is') + 3, item.length)
                        urlLink += '&except_i=' + app_x
                    }
                }
            }
            urlLink = 'http://127.0.0.1:8089/' + urlLink
            //urlLink = 'https://server-dash.herokuapp.com/' + urlLink
            console.log(urlLink)
            let myURL = "https://jsonplaceholder.typicode.com/comments"
            apply.innerHTML = ``
            apply.innerHTML = `<span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>
        Loading`
            apply.setAttribute('disabled', 'disabled');
            fetchDetails(urlLink)
        } else {
            alert(`Invalid ordering of Date-Time!`)
        }
    }

});

function delNote(index) {
    //console.log(index);
    //console.log(localStorage)
    let notes = localStorage.getItem('chips');
    if (notes == null) {
        chipList = [];
    } else {
        chipList = JSON.parse(notes);
    }



    chipList.splice(parseInt(index), 1);
    localStorage.setItem('chips', JSON.stringify(chipList));
    let filters = document.getElementById('filters')
    filters.innerHTML = ``

    chipList.forEach(function (element, index) {

        let chip = `<div class="chip my-2 mx-2">
        ${element}
        <span class="closebtn" id='${index}' onclick="delNote(this.id)">&times;</span>
    </div>`
        filters.innerHTML += chip;
    });
    chipSet = new Set(chipList)
    //console.log(chipSet)
    let val = document.getElementsByClassName('mydiv')[0].offsetHeight;
    document.getElementById('count').style.marginTop = val + "px"
}
function changeButton() {
    apply.innerHTML = `Apply`
    apply.removeAttribute('disabled', 'disabled');
}

function fetchDetails(lk) {
    $.ajax({
        url: lk,
        cache: false,
        type: "GET",
        success: function (response) {
            // console.log(response)
            // console.log(response.length)
            let res = JSON.parse(response)
            //console.log(res.length)
            let val = document.getElementsByClassName('mydiv')[0].offsetHeight - 0;
            document.getElementById('count').style.marginTop = val + "px"
            let tableContent = document.getElementById('contents')
            if (res.length > 0) {

                tableContent.innerHTML = `<thead class="thead-dark" style='margin-top:${val+5}px'>
    <tr>
      <th scope="col" style='font-size: 15px'>Timestamp </th>
      <th scope="col" style='font-size: 15px'>App Name</th>
      <th scope="col" style='font-size: 15px'>Exception Name</th>
      <th scope="col" style='font-size: 15px'>Error Message</th>
      <th scope="col" style='font-size: 15px'>Exception Details</th>
    </tr>
  </thead><tbody>`
//   th {
//     position: sticky;
//     top: 50px;  /* 0px if you don't have a navbar, but something is required */
//     background: white;
//   }
                appsMap.clear()
                exceptionMap.clear()
                appsSize = 0
                exceptionSize = 0
                appList = []
                exceptionList = []
                console.log(res)
                res.forEach(function (element) {

                    if (appsMap.get(element['cf_app_name']) == undefined) {
                        appsMap.set(element['cf_app_name'], 1)
                        appsSize = appsSize + 1
                        appList.push(element['cf_app_name'])
                    }
                    else appsMap.set(element['cf_app_name'], appsMap.get(element['cf_app_name']) + 1)

                    if (exceptionMap.get(element['Exception_Name']) == undefined) {
                        exceptionMap.set(element['Exception_Name'], 1)
                        exceptionSize = exceptionSize + 1
                        exceptionList.push(element['Exception_Name'])
                    }
                    else exceptionMap.set(element['Exception_Name'], exceptionMap.get(element['Exception_Name']) + 1)

                    //let chip = `<td>${element['postId']}</td><td>${element['name']}</td><td>${element['email']}</td><td>${element['body']}</td>`
                    let chip = `<tr><td>${element['timestamp8601']}</td><td>${element['cf_app_name']}</td><td>${element['Exception_Name']}</td><td>${element['Error_Message']}</td><td>${element['Exception_Details']}</td></tr>`
                    tableContent.innerHTML += chip;
                });
                tableContent.innerHTML += `</tbody>`
                document.getElementById('count').innerHTML = 'Total Count - ' + res.length
                console.log(appsSize)
                console.log(exceptionSize)
                setTimeout(changeButton(), 10000);
            } else {
                tableContent.innerHTML = `<h3 style="text-align:center;">No Results found!</h3>`
                document.getElementById('count').innerHTML = ''
                setTimeout(changeButton(), 10000);
            }
        },
        error: function (xhr) {

        }
    });
}
function showChips() {
    //console.log(localStorage)
    let notes = localStorage.getItem('chips');
    if (notes == null) {
        chipList = [];
    } else {
        chipList = JSON.parse(notes);
    }


    let filters = document.getElementById('filters')
    filters.innerHTML = ``
    chipSet = new Set(chipList)
    chipList.forEach(function (element, index) {

        let chip = `<div class="chip my-2 mx-2">
        ${element}
        <span class="closebtn" id='${index}' onclick="delNote(this.id)">&times;</span>
    </div>`
        filters.innerHTML += chip;
    });
    //console.log(chipSet)
    let val = document.getElementsByClassName('mydiv')[0].offsetHeight;
    document.getElementById('count').style.marginTop = val + "px"
}
document.getElementById('query').addEventListener('input', function (e) {
    console.log(e)
    let input;
    let filter;
    let table;
    let tr;
    let td;
    let i;
    let count = 0;
    let textVal;
    input = document.getElementById('query')
    filter = input.value.toUpperCase();
    table = document.getElementById('contents')
    tr = table.getElementsByTagName('tr')
    for (i = 0; i < tr.length; i++) {
        let isFound = false;
        td = tr[i].getElementsByTagName('td')[2]
        console.log(td)
        if (td) {
            textVal = td.textContent || td.innerText;
            if (textVal.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
                count = count + 1
                isFound = true;

            } else {
                tr[i].style.display = "none"
            }
        }
        // if (isFound == false) {
        //     td = tr[i].getElementsByTagName('td')[3]
        //     console.log(td)
        //     if (td) {
        //         textVal = td.textContent || td.innerText;
        //         if (textVal.toUpperCase().indexOf(filter) > -1) {
        //             tr[i].style.display = "";
        //             count = count + 1
        //             isFound = true;

        //         } else {
        //             tr[i].style.display = "none"
        //         }
        //     }
        // }
        // if (isFound == false) {
        //     td = tr[i].getElementsByTagName('td')[4]
        //     console.log(td)
        //     if (td) {
        //         textVal = td.textContent || td.innerText;
        //         if (textVal.toUpperCase().indexOf(filter) > -1) {
        //             tr[i].style.display = "";
        //             count = count + 1
        //             isFound = true;

        //         } else {
        //             tr[i].style.display = "none"
        //         }
        //     }
        // }
    }
    document.getElementById('count').innerHTML = 'Total Count - ' + count
});

