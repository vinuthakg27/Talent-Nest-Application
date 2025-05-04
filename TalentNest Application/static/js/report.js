document.addEventListener('DOMContentLoaded', function () {
  fetch('/api/report')
    .then(response => response.json())
    .then(data => {
      const tbody = document.querySelector('#report-table tbody');
      tbody.innerHTML = ''; // Clear existing rows

      data.forEach(row => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>${row.student_name}</td>
          <td>${row.college}</td>
          <td>${row.job_role}</td>
          <td>${row.company}</td>
          <td>${row.package}</td>
          <td>${row.status}</td>
        `;
        tbody.appendChild(tr);
      });
    })
    .catch(error => {
      console.error('Error fetching report data:', error);
    });
});
