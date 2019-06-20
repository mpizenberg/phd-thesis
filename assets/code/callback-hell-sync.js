// With theoretical blocking and synchronous APIs.
function getDataSync(url, id) {
  db = getDatabase(url);
  return db.get(id);
}

// How calling the function would look like.
try {
  data = getDataSync("some_url", 42);
  doSomethingWith(data);
} catch (error) {
  console.log(error);
}
