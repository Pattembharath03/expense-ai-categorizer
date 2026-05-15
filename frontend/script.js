async function predictExpense() {

    // Get input
    const text =
        document.getElementById("expense").value;

    // Send request
    const response = await fetch(

        "http://127.0.0.1:5000/predict",

        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                text: text
            })
        }
    );

    // Receive response
    const data = await response.json();

    // Display category
    document.getElementById("result").innerHTML =

        "Category: " + data.category;
}