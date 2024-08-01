class Solution {
    public int countSeniors(String[] details) {
        
        int counter = 0;
        Integer newNum;
        
        for(String detail : details){
            String num = detail.substring(11,13);
            newNum = Integer.parseInt(num);
            if(newNum > 60){
                counter++;
            }
        }
        
        return counter;
    }
}