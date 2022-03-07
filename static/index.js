function calculateTax() {
    var value0 = document.getElementById("value0").value;
    var value1 = document.getElementById("value1").value;
    var value2 = document.getElementById("value2").value;
    var value3 = document.getElementById("value3").value;
    var value4 = document.getElementById("value4").value;
    var value5 = document.getElementById("value5").value;
    var value6 = document.getElementById("value6").value;

    var result = document.querySelector('.btn');
    result.classList.add('show');

    var url = "/calculateTax";

    axios({
        method: "post",
        url: url,
        data: {
            value0: value0,
            value1: value1,
            value2: value2,
            value3: value3,
            value4: value4,
            value5: value5,
            value6: value6,
        },
        headers: {
            "Content-Type": "application/json",
        }
    }).then(
        (response) => {
            var result = response.data;
            console.log(response);
            document.getElementById("result0").innerHTML = result["result0"];
            document.getElementById("result1").innerHTML = result["result1"];
            document.getElementById("result2").innerHTML = result["result2"];
            document.getElementById("result3").innerHTML = result["result3"];
            document.getElementById("result4").innerHTML = result["result4"];
            document.getElementById("result5").innerHTML = result["result5"];
            document.getElementById("result6").innerHTML = result["result6"];
            document.getElementById("result7").innerHTML = result["result7"];
        },
        (error) => {
            console.log(error);
        }
    );
}

function reset() {
    var value0 = document.getElementById("value0").value;
    var value1 = document.getElementById("value1").value;
    var value2 = document.getElementById("value2").value;
    var value3 = document.getElementById("value3").value;
    var value4 = document.getElementById("value4").value;
    var value5 = document.getElementById("value5").value;
    var value6 = document.getElementById("value6").value;
    
    value0 = "";
    value1 = "";
    value2 = "";
    value3 = "";
    value4 = "";
    value5 = "";
    value6 = "";
}

function addClass() {
    var result = document.querySelector('.btn');
    result.classList.remove('show');
    result.classList.add('hide')

    var container = document.querySelector('.result');
    container.classList.remove('show');
    container.classList.add('hide')
}

function result() {
    var container = document.querySelector('.result');
    container.classList.add('show');
}
