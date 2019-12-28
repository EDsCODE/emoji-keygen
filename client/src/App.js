import React, { Component } from "react";
import "./App.css";
import { CONFIG } from "./config";
import Button from "@material-ui/core/Button";
import Textfield from "@material-ui/core/TextField";
import { Panel, Resultbox } from "./components";

export default class App extends Component {
    constructor() {
        super();
        this.state = {
            name: "",
            returned_emoji_key: "",
            emoji_sequence: "",
            returned_name: "",
            error: ""
        };
    }

    submitName = () => {
        if (this.state.name.length == 0) {
            this.clearState();
            return;
        }

        fetch(CONFIG.API_URL + "emoji", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ name: this.state.name })
        })
            .then(results => results.json())
            .then(jsonResult =>
                this.setState({ returned_emoji_key: jsonResult["encoded"] })
            )
            .catch(err => console.log(err));
        this.clearState();
    };

    submitEmojiSequence = () => {
        var url = new URL(CONFIG.API_URL + "info"),
            params = { key: this.state.emoji_sequence.trim() };

        Object.keys(params).forEach(key =>
            url.searchParams.append(key, params[key])
        );
        fetch(url, {
            method: "GET"
        })
            .then(results => {
                if (results.status != 200) {
                    this.handleError(results.status);
                }
                return results.json();
            })
            .then(jsonResult =>
                this.setState({ returned_name: jsonResult["decoded_address"] })
            )
            .catch(err => console.log("ERROR:", err));
        this.clearState();
    };

    handleError = code => {
        if (code == 404) {
            this.setState({
                error: "No associated key"
            });
        } else {
            this.setState({
                error: "Invalid request"
            });
        }
    };

    handleOnTextChange = (event, field) => {
        this.setState({
            [`${field}`]: event.target.value
        });
    };

    clearState = () => {
        this.setState({
            name: "",
            returned_emoji_key: "",
            emoji_sequence: "",
            returned_name: "",
            error: ""
        });
    };

    render() {
        return (
            <div className="App">
                <div className="input-section">
                    <Panel>
                        <h1>Emoji keygen</h1>
                        <p>
                            <b>Enter your name to generate a key</b>
                        </p>
                        <Textfield
                            className="input-field"
                            onChange={event =>
                                this.handleOnTextChange(event, "name")
                            }
                            value={this.state.name}
                            id="outlined-basic"
                            label="Your name"
                            variant="outlined"
                        ></Textfield>
                        <div className="input-button">
                            <Button
                                variant="contained"
                                color="primary"
                                onClick={this.submitName}
                            >
                                Generate Key
                            </Button>
                        </div>

                        <p>
                            <b>Enter your emoji key to retrieve information</b>
                        </p>
                        <Textfield
                            className="input-field"
                            onChange={event =>
                                this.handleOnTextChange(event, "emoji_sequence")
                            }
                            value={this.state.emoji_sequence}
                            id="outlined-basic"
                            label="Your emoji sequence"
                            variant="outlined"
                        ></Textfield>
                        <div className="input-button">
                            <Button
                                variant="contained"
                                color="primary"
                                onClick={this.submitEmojiSequence}
                            >
                                Retrieve
                            </Button>
                        </div>
                    </Panel>
                </div>
                <div className="result-section">
                    <Resultbox color="lightskyblue">
                        <h4>Sempo Emoji keygen challenge!</h4>

                        <p2>
                            <b>Generating a key:</b> Start by entering a name
                            into the first field. Submitting the name will
                            generate an emoji sequence that masks a private key
                            based on the Ethereum private key format (64 hex
                            characters)
                        </p2>
                        <p2>
                            <b>Retrieving the name:</b>The returned sequence of
                            emojis can be used to retrieve account related
                            information. In this example implementation the
                            server will return the associated name that was
                            input.
                        </p2>
                    </Resultbox>
                    {this.state.returned_emoji_key != null &&
                    this.state.returned_emoji_key.length > 0 ? (
                        <Resultbox color="lightgreen">
                            <p2>
                                <b>Emoji sequence: </b>
                                {this.state.returned_emoji_key}
                            </p2>
                        </Resultbox>
                    ) : null}
                    {this.state.returned_name != null &&
                    this.state.returned_name.length > 0 ? (
                        <Resultbox color="lightgreen">
                            <p2>
                                <b>Stored name: </b>
                                {this.state.returned_name}
                            </p2>
                        </Resultbox>
                    ) : null}
                    {this.state.error != null && this.state.error.length > 0 ? (
                        <Resultbox color="lightpink">
                            <p2>
                                <b>Error: </b>
                                {this.state.error}
                            </p2>
                        </Resultbox>
                    ) : null}
                </div>
            </div>
        );
    }
}
