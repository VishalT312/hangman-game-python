function calculateAge() {
    let dob = document.getElementById("dob").value;
    if (dob === "") {
      document.getElementById("result").innerHTML = "Please select your date of birth!";
      return;
    }
  
    let dobDate = new Date(dob);
    let today = new Date();
  
    let years = today.getFullYear() - dobDate.getFullYear();
    let months = today.getMonth() - dobDate.getMonth();
    let days = today.getDate() - dobDate.getDate();
  
    // Adjust days and months if needed
    if (days < 0) {
      months--;
      // Get the number of days in the previous month
      let prevMonth = new Date(today.getFullYear(), today.getMonth(), 0);
      days += prevMonth.getDate();
    }
  
    if (months < 0) {
      years--;
      months += 12;
    }
  
    document.getElementById("result").innerHTML = 
      `Your age is <b>${years}</b> years, <b>${months}</b> months, and <b>${days}</b> days old.`;
  }
  