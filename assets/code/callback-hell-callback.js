// With callback asynchronous APIs.
function getDataAsync(url, id, callback) {
  getDatabase(url, function(error, db) {
    if (error) {
      callback(error, null);
    } else {
      db.get(id, function(error, data) {
        if (error) {
          callback(error, null);
        } else {
          callback(null, data);
        }
      });
    }
  });
}

// How calling the function would look like.
getDataAsync("some_url", 42, function(error, data) {
  if (error) {
    console.log(error);
  } else {
    doSomethingWith(data);
  }
});
