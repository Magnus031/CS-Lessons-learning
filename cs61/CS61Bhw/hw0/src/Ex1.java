public class Ex1 {
    public static void main(String[] args) {
        for(int i=1;i<=5;i++){
            String L = "";
            for(int j=1;j<=i;j++)
                L+="*";
            System.out.println(L);
        }
    }
}
