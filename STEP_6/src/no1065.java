import java.util.Scanner;

public class no1065 {
		public static void main(String[] args) {
			Scanner in = new Scanner(System.in);
			int num=in.nextInt();
			int count=0;
			
			for(int i=1;i<=num;i++) {
				if(checkNum(i)) {
					//System.out.println(i);
					count++;
				}
			}
			
			System.out.println(count);
		}
		
		static boolean checkNum(int num) {
			int temp1=num%10;
			int temp2=(num%100)/10;
			int temp3=num/100;
			
			if(temp3==0&&temp2==0) return true;
			else if(temp3==0) return true;
			
			else {
				if((temp3-temp2)==(temp2-temp1)) return true;
				else return false;
			}
		}
}
