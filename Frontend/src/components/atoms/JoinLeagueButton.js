import React, { Component, useState } from "react";
import {
    Button,
    Dialog,
    DialogTitle,
    List,
    ListItem
 } from '@mui/material';


export default function JoinLeagueButton(props){
    const csrftoken = props.getCookie('csrftoken')
    const [teams, setTeams] = useState()
    const [open, setOpen] = useState(false)
    
    function handleRequestToJoinLeague(){
        const requestOptions = {
            method : 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFTOKEN' : csrftoken,
            },
            body: JSON.stringify(
                {'betting_league_id' : props.league_id}
            )
        }

        fetch('/api/betting/request-to-join-league', requestOptions)
        .then((response) => {
            response.json()
            .then((json) => {
                console.log(json)
                setTeams(json);
                setOpen(true)   
            })
        })
    }

    function handleTeamSelected(e){
        const selectedTeamId = e.target.getAttribute('value')
        setOpen(false);

        const requestOptions = {
            method : 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFTOKEN' : csrftoken,
            },
            body: JSON.stringify(
                {
                    'fantasy_team_id' : selectedTeamId,
                    'betting_league_id' : props.league_id
                }
            )
        }


    }

    return (
        <>
            <Button
                onClick={handleRequestToJoinLeague}
            >
                Join
            </Button>
            <Dialog
                open={open}
                onClose={() => setOpen(false)}
            >
            <DialogTitle> Select Your Team </DialogTitle>
            <List>
                {teams?.map((team, index) => {
                    return (
                    <ListItem button value={team.id} onClick={handleTeamSelected}>
                        {team.fun_name}
                    </ListItem>
                    )
                })}
                <ListItem button> - Not an Owner - </ListItem>
            </List>
            </Dialog>
            
        </>
    )
}