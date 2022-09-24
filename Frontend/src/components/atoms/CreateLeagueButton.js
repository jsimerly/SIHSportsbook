import React, { Component, useState } from "react";
import {
    Button,
    Dialog,
    DialogTitle,
    InputLabel,
    Input,
    DialogActions
 } from '@mui/material';


export default function JoinLeagueButton(props){
    const csrftoken = props.getCookie('csrftoken')
    const [leagueName, setLeagueName] = useState()
    const [open, setOpen] = useState(false)
   
    function handleCreateLeaguePressed(e){
        setOpen(false)
        console.log(props.league_id)
        console.log(leagueName)
        
        const requestOptions = {
            method : 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFTOKEN' : csrftoken,
            },
            body: JSON.stringify(
                {
                    'fantasy_league_id' : props.league_id,
                    'betting_league_name' : leagueName
                }
            )
        }

        fetch('/api/betting/create-betting-league', requestOptions)
        .then((response) => {
            console.log(response)
        })
    }

    return (
        <>
            <Button
                onClick={() => setOpen(true)}
            >
                Create
            </Button>
            <Dialog
                open={open}
                onClose={() => setOpen(false)}
            >
            <DialogTitle> Enter Betting League's Name: </DialogTitle>
            <InputLabel> League Name</InputLabel>
            <Input onChange={(e) => setLeagueName(e.target.value)}/>
            <DialogActions>
                <Button onClick={handleCreateLeaguePressed}> Create League</Button>
                <Button onClick={() => setOpen(false)}> Cancel </Button>
            </DialogActions>
            
            </Dialog>
            
        </>
    )
}