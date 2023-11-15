import React, { Component } from "react";
import ReactDOM from "react-dom";
import "react-responsive-carousel/lib/styles/carousel.min.css"; // requires a loader
import { Carousel } from "react-responsive-carousel";

class DemoCarousel extends Component {
  render() {
    return (
      <div style={{ width: "500px" }}>
        <Carousel>
          <div>
            <img src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/jrfyzvgzvhs1iylduuhj.jpg" />
            <p className="legend">Hong Kong</p>
          </div>
          <div>
            <img src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/c1cklkyp6ms02tougufx.webp" />
            <p className="legend">Macao</p>
          </div>
          <div>
            <img src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/e8fnw35p6zgusq218foj.webp" />
            <p className="legend" alt="Japan">
              Japan
            </p>
          </div>
          <div>
            <img
              src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/liw377az16sxmp9a6ylg.webp"
              alt="Las"
            />
            <p className="legend">Las Vegas</p>
          </div>
        </Carousel>
      </div>
    );
  }
}

// ReactDOM.render(<DemoCarousel />, document.querySelector(".demo-carousel"));

export default DemoCarousel;
