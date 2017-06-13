import java.io.*;
import java.util.*;
import java.text.*;

class writeTest
{
	static BufferedReader br = null;
	static int finalCount = 0;
	public static void main(String[] args)
	{
		csvReader();
	}
	public static void csvReader()
	{
		String csvFile = "C:\\Users\\arpit\\Documents\\GitHub\\GSoC-Strain_Diffrential\\log.txt";
		String line = "";		

		try
		{
			br = new BufferedReader(new FileReader(csvFile));
			int counter = 0;
			while((line=br.readLine()) != null)
			{
				if (line.length() > 0){
				if(line.charAt(0) == 'C' && line.length() < 2)
					counter++;
				else
				{
					if(counter>finalCount)
						finalCount = counter;
					counter = 0;

				}
			} 	
			}
			System.out.print("\n" + finalCount);
		}
		catch (FileNotFoundException e) 
		{
			e.printStackTrace();
		} 
		catch (IOException e) 
		{
			e.printStackTrace();
		} 
		finally 
		{
			if (br != null) {
				try 
				{
					br.close();
				} 
				catch (IOException e) 
				{
					e.printStackTrace();
				}
			}
		}
	}
}