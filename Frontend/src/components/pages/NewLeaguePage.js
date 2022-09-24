import React, { useState, useEffect } from  "react";
import {
    useNavigate,
} from "react-router-dom";
import { 
    Button, 
    Grid, 
    Typography, 
    FormControl,
    Input,
    InputLabel,
    Box,
 } from '@mui/material';
import SearchLeagueResults from "../organisms/SearchLeagueResults";

export default function NewLeaguePage(props){
    const [sleeperId, setSleeperId] = useState() //793159261780803584 784444797430657024 735889493080666112
    const [leagues, setLeagues] = useState(null)
    const csrftoken = props.getCookie('csrftoken')


    function handleSearchPressed(){
        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type' : 'application/json',
                'X-CSRFTOKEN' : csrftoken,
            },
            body: JSON.stringify({
                'sleeper_id' : sleeperId,
            })
        }

        fetch('/api/fantasy/find-leagues', requestOptions)
        .then((response) => {
            if (response.status===200) {
                response.json()
                .then((data) => {
                    setLeagues(data)
                })                
            } else {
                setError(response.json())
            }
        })
    }

    function handleLeagueIdChanged(e){
        setSleeperId(e.target.value)
    }

    function ifSearchResutls(){
        if (leagues != null){
            return (
                <Grid 
                    item xs={12} 
                    align="center" 
                    container
                >
                    <SearchLeagueResults
                        leagues={leagues}
                        getCookie={props.getCookie}
                    /> 
                </Grid>
            )
        } else {
            return (<div></div>)
        }
    }

    return (
        <Box 
            sx={{mt:5, width: '35%',}} 
            justifyContent="center"
            alignItems="center"
        >
            <Grid container spacing={1}>
                <Grid item xs={12} align="center">
                    <Typography component='h5' variant='h5'>
                        Create or Find a League: 
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <FormControl sx={{minWidth: '40%'}}>
                        <InputLabel> Sleeper League Id </InputLabel>
                        <Input
                            onChange={handleLeagueIdChanged}
                        />
                    </FormControl>
                </Grid>
             
                <Grid item xs={12} align="center">
                    <Button
                        variant="contained"
                        color="primary"
                        onClick={handleSearchPressed}
                    >
                        Search
                    </Button>
                </Grid>
                {ifSearchResutls()}
            </Grid>
        </Box>
    )
}