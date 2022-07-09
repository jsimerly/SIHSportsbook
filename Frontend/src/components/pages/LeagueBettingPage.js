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
    const [parlayStatus, setParlayStatus] = useState(false);
    const [readyBets, setReadyBets] = useState([]);
    const [parlayWager, setParlayWager] = useState(0);
    const csrftoken = props.getCookie('csrftoken')

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

    function betReadyHandler(wager, bet) {
        let newBetArr = readyBets;
        const dupIndex = checkDupsIndex(newBetArr, bet)

        if (wager != 0 || wager != ''){
            if (dupIndex != -1){
                newBetArr[dupIndex].betData.wager = wager
            } else {
                bet.betData.wager = wager
                newBetArr.push(bet)
            }
        } else {
            newBetArr.splice(dupIndex,1)
        }
        setReadyBets([...newBetArr])
        console.log(readyBets)
    }

    function handleParlayToggle(parlayStatus){
        let newReadyBets = [];
        if (parlayStatus){
            console.log(parlayWager)  
            if (parlayWager != 0 || parlayWager != ''){
                newReadyBets = selectedBets
            } 
        } else {
            selectedBets.map((bet, index) => {
                console.log('non par')
                console.log(bet.betData.wager)
                if (bet.betData.wager != 0 || bet.betData.wager != '' || bet.betData.wager != "0"){
                    console.log('push')
                    newReadyBets.push(bet)
                }
            })
        }
        console.log(newReadyBets)
        setReadyBets([...newReadyBets])
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

    function createBetsMap(bets){
        let bets_info = []
        
        bets.map((bet, index) => {

            let info_map = {
                bettorId : props.currentLeague.bettor_id,
                matchupId : bet.matchupData.matchupId,
                betAmount : bet.betData.wager,
                betType : bet.betData.betType,
            }

            bets_info.push(info_map)
        })

        let post_data = {
            "parlay" : parlayStatus,
            "parlay_wager" : parlayWager,
            "bets" : bets_info
        }

        return post_data
    }

    function handleSubmitBets(){     
        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFTOKEN' : csrftoken,
            },
            body: JSON.stringify(
                createBetsMap(readyBets)
                
            )
        }

        fetch('/api/betting/place-bet-matchup', requestOptions)
        .then((response) => {
            console.log(response.json())
        })
    }


    function handleParlayStatus(status){
        setParlayStatus(status)
    }

    function handleParlayWager(wager){
        setParlayWager(wager)
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
                        handleSubmitBets={handleSubmitBets}
                        selectedBets={selectedBets}
                        handleWager={betReadyHandler}
                        handleParlayToggle={handleParlayToggle}
                        handleParlayWager={handleParlayWager}
                        handleParlayStatus={handleParlayStatus}
                    />
                </Grid>
            </Grid>
        </div>
    )
}