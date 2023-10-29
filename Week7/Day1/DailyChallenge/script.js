class Video {
  constructor(title, uploader, time) {
    this.title = title;
    this.uploader = uploader;
    this.time = time;
  }
  watch() {
    return `${this.uploader} watched all ${this.time} of ${this.title}`;
  }
}

const video1 = new Video("Matrix", "Jack", 7200);
const video2 = new Video("Harry Potter", "John", 6500);
console.log(video1.watch());
console.log(video2.watch());
// console.log(video1.watch())
const videoDataArray = [
  { title: "Video1", uploader: "Uploader1", time: 1200 },
  { title: "Video2", uploader: "Uploader2", time: 1800 },
  { title: "Video3", uploader: "Uploader3", time: 2400 },
  { title: "Video4", uploader: "Uploader4", time: 3000 },
  { title: "Video5", uploader: "Uploader5", time: 3600 },
];

const videoInstancesArray = [];
for (let i = 0; i < videoDataArray.length; i++) {
  const { title, uploader, time } = videoDataArray[i];
  const video = new Video(title, uploader, time);
  videoInstancesArray.push(video);
}
console.log(videoInstancesArray);
