export const formatPrice = (price = 0, currency = 'USD') => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: currency,
    }).format(price);
  };

export const formatNumber = (number) => {
  return new Intl.NumberFormat().format(number);
}