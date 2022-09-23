import React, { Component } from "react";
import {
  
    Button,
 } from '@mui/material';


export default function CreateLeagueButton(props){
    const csrftoken = props.getCookie('csrftoken')
    // function handleSubmitCreateLeague(bettingLeagueId){
    //     const requestOptions = {
    //         method: 'POST',
    //         headers: {
    //             'Content-Type': 'application/json',
    //             'X-CSRFTOKEN' : csrftoken,
    //         },
    //         body: JSON.stringify(
    //             'betting_league_id' = bettingLeagueId,
    //         )
    //     }

    // }
  
    return (
        <Button
           // onClick={handleSubmitCreateLeague(props.league_id)}
        >
            Create
        </Button>
    )
}