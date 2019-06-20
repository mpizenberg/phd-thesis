// With new async/await keywords and APIs.
async function getDataSync(url, id) {
  db = await getDatabase(url);
  data = await db.get(id);
  return data;
}

// How calling the async function looks like.
try {
  data = await getDataSync("some_url", 42);
  doSomethingWith(data);
} catch (error) {
  console.log(error);
}
