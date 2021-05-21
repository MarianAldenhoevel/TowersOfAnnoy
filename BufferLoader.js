function BufferLoader(audio_context, url_list, callback) {
  this.audio_context = audio_context;
  this.url_list = url_list;
  this.onload = callback;
  this.buffer_list = new Array();
  this.loadCount = 0;
}

// Buffer loader taken from http://www.html5rocks.com/en/tutorials/webaudio/intro/js/buffer-loader.js
BufferLoader.prototype.loadBuffer = function(url, index) {
  // Load buffer asynchronously
  var request = new XMLHttpRequest();
  request.open("GET", url, true);
  request.responseType = "arraybuffer";

  var loader = this;

  request.onload = function() {
    // Asynchronously decode the audio file data in request.response
    loader.audio_context.decodeAudioData(
      request.response,
      function(buffer) {
        if (!buffer) {
          console.log('error decoding file data: ' + url);
          return;
        }
        loader.buffer_list[index] = buffer;
        if (++loader.loadCount == loader.url_list.length)
          loader.onload(loader.buffer_list);
      },
      function(error) {
        console.log('decodeAudioData error');
      }
    );
  }

  request.onerror = function() {
    alert('BufferLoader: XHR error');
  }

  request.send();
}

BufferLoader.prototype.load = function() {
  for (var i = 0; i < this.url_list.length; ++i) {
    this.loadBuffer(this.url_list[i], i);
  }
}
