import java.util.Arrays;
import java.util.Scanner;
import java.util.Comparator;

public class solution{

    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        singer singers[] = new singer[n];
        for(int i=0; i<n; i++)
        {
            singers[i] = new singer();
            singers[i].id = i;
            singers[i].lb = s.nextInt();
            singers[i].ub = s.nextInt();
        }

        Arrays.sort(singers);

        for(int i=0; i<n; i++) singers[i].score = (n-1-i)*2;

        Comparator<singer> cmp = new Comparator<singer>(){
            public int compare(singer s1, singer s2){
                return s1.id - s2.id;
            }
        };

        Arrays.sort(singers, cmp);
        for(int i=0; i<n; i++)
        {   if(i==n-1) System.out.print(singers[i].score + "\n");
            else
            System.out.print(singers[i].score + " ");}

    }

}

class singer implements Comparable<singer>{
    int lb;
    int ub;
    int id;
    int score;
    public int compareTo(singer s2){
        return this.lb - s2.lb;
    }
}