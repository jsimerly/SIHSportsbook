import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import DrawerComp from "../organisms/Drawer";
import Matchups from "../organisms/Matchups";
import BetSlip from "../organisms/BetSlip";
import {
    Box,
    Grid
} from '@mui/material'


export default function LeagueBettingPage(props){
    const { leagueId } = useParams()

    useEffect(() => {
        getMatchups()
    }, [props.currentLeague])

    const [matchupJson, setMatchupJson] = useState([]);
    const [selectedBets, setSelectedBets] = useState([]);

    function getMatchups(){
        fetch('/api/betting/get-matchups' + "?league-id=" + leagueId)
        .then((response) => {
            if (!response.ok) {
                console.log('error')
            }
            return response.json()
        })
        .then((data) => {
            setMatchupJson(data);
            
        })
    }

   

    function checkDupsIndex(betArray, newBet) {
        for (var i=0; i < betArray.length; i++) {
            const betId = betArray[i].matchupData.id
            const newBetId = newBet.matchupData.id
            const betType = betArray[i].betData.betType
            const newBetType = newBet.betData.betType

            if (betId == newBetId && betType == newBetType) {
                return i
            }
        }
        return -1
    }

    function betSelectedHandler(newBet) {
        let newBetArr = selectedBets;
        const dupIndex = checkDupsIndex(newBetArr, newBet)

        if (dupIndex != -1) {
            newBetArr.splice(dupIndex,1)
        } else {
            newBetArr.push(newBet)
        }
        setSelectedBets([...newBetArr])
    }

    function handleRemoveBet(removedBet) {
        const dupIndex = checkDupsIndex(selectedBets, removedBet)
        setSelectedBets([
            ...selectedBets.slice(0, dupIndex),
            ...selectedBets.slice(dupIndex + 1)
        ])
    }

    function handleRemoveAllBets() {
        setSelectedBets([])
    }

    return (
        
        <div>
            <Grid container>
                <Grid item>
                    <Box sx={{width: 250, height: '100vh', border:1 }}>
                        <DrawerComp
                            setLeague={props.setLeague}
                            leagues={props.leagues}
                            currentLeague={props.currentLeague}
                        />
                    </Box>
                </Grid>
                <Grid margin={2} md={7} spacing={1} sx={{border:1}}>
                    <Matchups 
                        data={matchupJson} 
                        betSelectedHandler={betSelectedHandler}
                        selectedBets={selectedBets}
                        checkDupsIndex={checkDupsIndex}
                    />
                </Grid>
                <Grid margin={2} md={2} spacing={1} sx={{border:1}}>
                    <BetSlip 
                        handleRemoveBet={handleRemoveBet} 
                        handleRemoveAllBets={handleRemoveAllBets}
                        selectedBets={selectedBets}
                    />
                </Grid>
            </Grid>
        </div>
    )
}