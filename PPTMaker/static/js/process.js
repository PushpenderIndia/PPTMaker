function checkTaskProgress(taskId) {
  // Create a new XMLHttpRequest object
  var xhr = new XMLHttpRequest();

  // Set the request URL and method
  xhr.open('GET', '/check_task_progress?task_id=' + taskId);

  // Set the response type to JSON
  xhr.responseType = 'json';

  // When the request is complete
  xhr.onload = function() {
    // If the status is success, initiate the file download
    if (xhr.status === 200 && xhr.response.status === 'SUCCESS') {
      file_path = window.location.href.split("/")[0] + "//"+ window.location.href.split("/")[2] + "/" + xhr.response.output_filepath
      console.log(file_path);
      window.location.href = file_path;
    } else if (xhr.response.status === 'FAILURE') {
      // The task failed, show an error message
      alert('Task failed');
    } else {
      // The task is still running, check again in 1 second
      setTimeout(function() {
        checkTaskProgress(taskId);
      }, 1000);
    }
  };

  // Send the request
  xhr.send();
}

  