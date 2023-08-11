function refresh()
{
    window.location.reload();
}

function getbookdata()
{
    $.ajax({
        url: "http://43.139.83.100:9001/getdata",
        type: "get",
        dataType: "json",
        data: JSON.stringify({

        }),
        success: function(data)
        {
            console.log(data);
            
            var booktable = document.getElementById("booktable");
            var booklist = data["data"]

            var updatetime = document.getElementById("updatetime");
            updatetime.innerHTML = booklist[0][7];
            for(var i = 0; i < booklist.length; i++)
            {
                var row = booktable.insertRow(-1);
                var bookname = row.insertCell(0);
                var writer = row.insertCell(1);
                var publisher = row.insertCell(2);
                var publishdate = row.insertCell(3);
                var price = row.insertCell(4);
                var rating = row.insertCell(5);
                var comments = row.insertCell(6);
                bookname.innerHTML = booklist[i][0];
                writer.innerHTML = booklist[i][1];
                publisher.innerHTML = booklist[i][2];
                publishdate.innerHTML = booklist[i][3];
                price.innerHTML = booklist[i][4];
                rating.innerHTML = booklist[i][5];
                comments.innerHTML = booklist[i][6];
            }
            

            // window.location.reload();
        },
        error: function()
        {
            alert("unknown error: please check server log information");
            console.trace();
        }
    })
}

function crawldata()
{
    alert("start crawling data......\nIt might take few seconds to update");
    $.ajax({
        url: "http://43.139.83.100:9001/crawldata",
        type: "post",
        dataType: "json",
        data: JSON.stringify({

        }),
        success: function(data)
        {
            console.log(data);
            alert("data crawling complete!!!\nPlease reload the page");
            refresh();
        },
        error: function()
        {
            alert("unknown error: please check server log information");
            console.trace();
        }
    })
}

function deletedata()
{
    $.ajax({
        url: "http://43.139.83.100:9001/deletedata",
        type: "post",
        dataType: "json",
        data: JSON.stringify({

        }),
        success: function(data)
        {
            console.log(data);
            alert(data["status"]);
            refresh();
        },
        error: function()
        {
            alert("unknown error: please check server log information");
            console.trace();
        }
    })
}