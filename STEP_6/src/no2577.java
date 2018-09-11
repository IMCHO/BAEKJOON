import java.util.Scanner;

public class no2577 {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int num=1;
		
		for(int i=0;i<3;i++) {
			num*=in.nextInt();
		}
		
		Integer temp=new Integer(num);
		String str=temp.toString();
		String[] strArr=str.split("");

		int[] arr= {0,0,0,0,0,0,0,0,0,0};
		for(String s : strArr) {
			arr[Integer.parseInt(s)]++;
		}
		
		for(Integer i : arr) {
			System.out.println(i);
		}
	}
}
