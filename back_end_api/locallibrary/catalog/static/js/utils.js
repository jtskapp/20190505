//alert('js loaded');

let draw = false;

$(document).ready(function() {
    loaddata();
    const tbl = $('#demo-table').DataTable();
    const tbl_data = getTableData(tbl);
    createHighcharts(tbl_data);
    setTableEvents(tbl);
} );


function loaddata() {

    var section = $('.table-section');
    var html = ''
    html += '<table id="demo-table" class="table table-responsive">'
    html += '<thead><tr>'
    html += '<th>Id</th><th>Author</th><th>Title</th><th>Summary</th><th>ISBN</th><th>PublicationDate</th><th>EntryDate</th><th>Total</th>'
    html += '</tr></thead>'
    html += '<tbody></tbody>'
    html += '</table>'

    section.html(html);


    $('#demo-table').DataTable( {
        "columns": [
            { "data": "id", "name": "Id", "title": "Id" },
            { "data": "author", "name": "Author", "title": "Author" },
            { "data": "title", "name": "Title", "title": "Title" },
            { "data": "summary", "name": "Summary", "title": "Summary" },
            { "data": "isbn", "name": "ISBN", "title": "ISBN" },
            { "data": "date_of_publication", "name": "PublicationDate", "title": "PublicationDate" },
            { "data": "date_of_entry", "name": "EntryDate", "title": "EntryDate" },
            { "data": "total_books", "name": "Total", "title": "Total" }
            ],
        "ajax": {
           url: 'http://127.0.0.1:8000/api/',
           method: "GET",
            dataSrc : function(json) {
//                console.log(json);
                var temp, item, data = [];
                for (var i=0;i<json.data.length;i++) {
                    temp = json.data[i]
                    item = {};
                    for (var elem in temp) {
                        if (elem == 'author') {
                            item[elem] = temp[elem]['first_name'] + ' ' + temp[elem]['last_name']
                        } else {
                            item[elem] = temp[elem]
                        }
                    }
                    data.push(item);
                }
                return data
            }
        },
        "drawCallback": function( settings ) {
//            alert('page draw');
//            alert( 'DataTables has redrawn the table' );
//            LoadChart();
        }
    } );

}

function setTableEvents(table) {
  // listen for page clicks
  table.on("page", () => {
    draw = true;
  });

  // listen for updates and adjust the chart accordingly
  table.on("draw", () => {
    if (draw) {
      draw = false;
    } else {
      const tableData = getTableData(table);
      console.log(tableData);
      createHighcharts(tableData);
    }
  });
}

function createHighcharts(data) {
  Highcharts.setOptions({
    lang: {
      thousandsSep: ","
    }
  });

  Highcharts.chart("chart-section", {
    title: {
      text: "DataTables to Highcharts"
    },
    subtitle: {
      text: "Books Listing"
    },
    xAxis: [
      {
        categories: data[0],
        labels: {
          rotation: -45
        }
      }
    ],
    yAxis: [
      {
        // first yaxis
        title: {
          text: "Number of Books"
        }
      },
//      {
//        // secondary yaxis
//        title: {
//          text: "Density (P/Km²)"
//        },
//        min: 0,
//        opposite: true
//      }
    ],
    series: [
      {
        name: "Number of Books",
        color: "#0071A7",
        type: "column",
        data: data[1],
//        tooltip: {
//          valueSuffix: " M"
//        }
      },
//      {
//        name: "Density (P/Km²)",
//        color: "#FF404E",
//        type: "spline",
//        data: data[2],
//        yAxis: 1
//      }
    ],
    tooltip: {
      shared: true
    },
    legend: {
      backgroundColor: "#ececec",
      shadow: true
    },
    credits: {
      enabled: false
    },
    noData: {
      style: {
        fontSize: "16px"
      }
    }
  });
}

function getTableData(table) {
  const dataArray = [],
    authorArray = [],
    totalBooksArray = [];

  // loop table rows
  table.rows({ search: "applied" }).every(function() {
    const data = this.data();
//    console.log(data);
    authorArray.push(data['author']);
    totalBooksArray.push(parseInt(data['total_books']));
  });

  // store all data in dataArray
  dataArray.push(authorArray, totalBooksArray);

  return dataArray;
}


function myclock() {
    document.querySelectorAll('.myclock')[0].innerHTML = moment().format("MMMM Do YYYY, hh:mm:ss a");
      function harold(standIn) {
        if (standIn < 10) {
          standIn = '0' + standIn
        }
        return standIn;
      }
} setInterval(myclock, 1000);


function estclock() {
    document.querySelectorAll('.estclock')[0].innerHTML = moment().
        tz("America/New_York").format("MMMM Do YYYY, hh:mm:ss a");
      function harold(standIn) {
        if (standIn < 10) {
          standIn = '0' + standIn
        }
        return standIn;
      }
} setInterval(estclock, 1000);

function gmtclock() {
    document.querySelectorAll('.gmtclock')[0].innerHTML = moment().
        tz("Europe/London").format("MMMM Do YYYY, hh:mm:ss a");
      function harold(standIn) {
        if (standIn < 10) {
          standIn = '0' + standIn
        }
        return standIn;
      }
} setInterval(gmtclock, 1000);