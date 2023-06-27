// script.js
// Add an event listener to the download button
document.getElementById("download-btn").addEventListener("click", function () {
    // Create a new jsPDF instance
    const doc = new jsPDF();

    // Get the HTML content to be converted to PDF
    const element = document.getElementById("test");

    // Convert the HTML content to PDF
    doc.html(element, {
        callback: function (pdf) {
            // Save the PDF file
            pdf.save("output.pdf");
        },
    });
});
