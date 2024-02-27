function deleteBill(button) {
    // This function will trigger when the 'Delete' button is clicked.
    const row = button.parentElement.parentElement; // Assuming the button is within a row you want to delete
    row.remove(); // This will remove the row from the DOM

    // Optionally, add your code here to handle other deletion tasks, like updating the database.
}
{
    // For demonstration, let's just alert the status
    alert('The status of this bill is: ' + statusCell.textContent);
    
    // If you want to mark it as paid:
    // statusCell.textContent = 'Paid';
    // statusCell.style.color = 'green';
}