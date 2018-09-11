import java.util.Scanner;

public class NUM_1152 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String str=in.nextLine();
		 
		int count=0;
		
		String[] strArr=str.split(" ");
		
		for(int i=0;i<strArr.length;i++) {
			if(!strArr[i].equals("")) count++;
		}
		System.out.println(count);
	}
}
