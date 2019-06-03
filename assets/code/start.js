// Set elm app flags
const flags = {
  deviceSize: containerSize(), // allocated layout space
  mturkMode: false, // true if embeded in mturk
  images: [], // array of preloaded images
  config: null // or preloaded Json config
};

// Start elm app.
const app = Elm.Main.fullscreen(flags)