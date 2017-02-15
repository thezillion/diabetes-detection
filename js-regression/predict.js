function std_deviation(X){ // X must be an array of numbers
	var mean = X.reduce(function(acc,val){
		return acc + val;
	},0);
	mean = mean / X.length;
	var sq_mean = X.reduce(function(acc,val){
		return acc + val*val;
	},0);
	sq_mean = sq_mean / X.length
	var mean_sq = mean*mean;
	return Math.sqrt(sq_mean - mean_sq);
}


function corelation(X,Y){
	return covariance(X,Y)/Math.sqrt(
			Math.pow(std_deviation(X),2)*
			Math.pow(std_deviation(Y),2)
		);
}

function mean(X){
	return X.reduce(function(acc,val){
		return acc + val;
	},0) / X.length;
}

function covariance(X,Y){
	const X_mean = mean(X),
		  Y_mean = mean(Y);
	return X.reduce(function(acc,val,i){
		return acc + (val - X_mean)*(Y[i] - Y_mean);
	},0)/ (X.length -1);
}


function get_prediction_function(X,Y){
	const mean_X = mean(X),
		  mean_Y = mean(Y),
		  sd_X   = std_deviation(X),
		  sd_Y   = std_deviation(Y),
		  r      = corelation(X,Y);
	const slope = r*(sd_Y/sd_X),
		  intercept = mean_Y - slope*mean_X;
	return function(X){
		return slope*X + intercept;
	};
}


var X = [1,2,3,4,5];
var Y = [1,2,1.3,3.75,2.25];

// console.log("std_deviation x:",std_deviation(X));
// console.log("std_deviation y:",std_deviation(Y));
// console.log("corelation:",corelation_coeff(X,Y));
console.log("prediction:",get_prediction_function(X,Y)(2.5));
