document.getElementById("submissionForm").addEventListener("submit", async function (event) {
    event.preventDefault();
  
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
  
    try {
      const response = await fetch("/submit", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, email }),
      });
  
      if (response.ok) {
        alert("Form data submitted successfully!");
      } else {
        alert("Form data submission failed. Please try again.");
      }
    } catch (error) {
      console.error("Error during form data submission:", error);
      alert("An error occurred. Please try again later.");
    }
  });
