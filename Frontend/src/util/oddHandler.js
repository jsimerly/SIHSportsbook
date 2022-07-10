export function impliedOddsToAmerican(odds){
    if (odds < .5){
        let americanOdds = ((1-odds)/(odds))*100
        americanOdds = Math.round(americanOdds)
        return "+" + americanOdds
    } else {
        let americanOdds = -100*((odds)/(1-odds))
        americanOdds = Math.round(americanOdds)
        return americanOdds
    }
}

export function getParlayOdds(bets, parlay_vig){
    let prob = 1
    bets.map((bet, index) => {
        prob *= bet.betData.odds
    })
   
    prob += parlay_vig
    
    return prob
}