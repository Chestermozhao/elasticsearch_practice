import React, { Component } from "react";
import Head from 'next/head';
import "../static/index.css";
import TitlePage from "-!svg-react-loader!../images/title_page.svg";
import axios from "axios";


export class Index extends Component {
  constructor() {
    super();
    this.state = {
      completeResult: [],
      barValue: "",
    };

    this.handleChange = this.handleChange.bind(this);
    this.updateBarValue = this.updateBarValue.bind(this);
  }

  updateBarValue(e) {
    var choosed_item = e.target.innerHTML;
    this.setState({completeResult: [], barValue: choosed_item})
  }

  handleChange(e) {
    var req_word = e.target.value;
    if (req_word) {
      axios.
        post("http://localhost:9200/wiki_prefix_search/_search/?size=5", {
            /* importance is set for phrase or word(no space in word):
               asc means word priority
               desc means phrase priority
            */
            sort: [
              {"importance" : "asc"}
            ],
            query: {
              prefix: {
                "word.keyword": req_word
              }
            }
          },
      )
        .then(response => {
          let respList = response.data.hits.hits;
          this.setState({
              completeResult: respList,
              barValue: req_word,
          })
        })
        .catch(error => console.log(error.message));
    } else {
      this.setState({completeResult: [], barValue: req_word})
    }
  }

  render() {
    const {completeResult, barValue} = this.state;
    return (
        <React.Fragment>
          <Head>
            <title>Chester's PrefixSearch Demo</title>
            <meta name="viewport" content="initial-scale=1.0, width=device-width" />
          </Head>
          <p className="title-center">Welcome to Chester's Elasticsearch search bar demonstration</p>
          <div className="input-center">
            <input type="text" className="input-style" value={barValue} onChange={this.handleChange} />
            <button className="button">Search</button>
          </div>
          <div className="search-result-box">
            {completeResult.map((wordItem, index)=>{
              return (
                <div key={index}>
                  <p className="search-result-item" onClick={this.updateBarValue}>
                    {wordItem._source.word}
                  </p>
                </div>
              )
            })}
          </div>
          <TitlePage className="center" />
        </React.Fragment>
    );
  }
}

export default Index;
